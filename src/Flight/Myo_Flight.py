from api_library import DroneController
from myo import init, Hub, Feed
import time

import myo as libmyo; 
import sys

drone1 = DroneController('b4d793f9680ba50d385e185b619eec0c0752347d', 'HNCnaCYD')
#drone2 = DroneController('746821f921735b2510a5653f31ace5dded0bf7d1', 'wDwpZXns')
#drone3 = DroneController('d7ef6762c83d16416b8f4f6ad93ede528546bb9b', 'jIuzqpPJ')


libmyo.init()

global on
on = True

global lastPose
lastPose = ""

global roll
roll = 0

global pitch 
pitch = 0

global yaw 
yaw = 0

global rollOff
rollOff = 0

global pitchOff
pitchOff = 0

class Listener(libmyo.DeviceListener):
    """
    Listener implementation. Return False from any function to
    stop the Hub.
    """
    
    interval = .15  # Output only 0.15 seconds

    def __init__(self):
        super(Listener, self).__init__()
        self.orientation = None
        self.pose = libmyo.Pose.rest
        self.emg_enabled = False
        self.locked = False
        self.rssi = None
        self.emg = None
        self.last_time = 0

    def output(self):
        global on
        global lastPose
        global roll
        global pitch
        global yaw
        global rollOff
        global pitchOff

        ctime = time.time()
        if (ctime - self.last_time) < self.interval:
            return
        self.last_time = ctime

        if self.orientation:
            pitch = self.orientation[0]
            roll = self.orientation[1]
            yaw = self.orientation[2]        

        print pitch

        multi = 3
        if (self.pose == "double_tap" and lastPose != "double_tap"):
            if(on):
              on = False
            else:
              on = True

        if (on):
          print drone1.velocity_set((multi*-roll), (multi*-pitch), 0.0, 0, 0, False, True, False, False)
          #print drone2.velocity_set((multi*-roll) - rollOff, (multi*-pitch) - pitchOff, 0.0, 0, 0, False, True, False, False)
          #print drone3.velocity_set((multi*-roll) - rollOff, (multi*-pitch) - pitchOff, 0.0, 0, 0, False, True, False, False)
        else:
          print drone1.velocity_set(0,0,0)
          #print drone2.velocity_set(0,0,0)
          #print drone3.velocity_set(0,0,0)

        lastPose = self.pose         

        sys.stdout.flush()


    def on_connect(self, myo, timestamp, firmware_version):
        myo.vibrate('short')
        myo.vibrate('short')
        myo.request_rssi()
        myo.request_battery_level()

    def on_rssi(self, myo, timestamp, rssi):
        self.rssi = rssi
        self.output()

    def on_pose(self, myo, timestamp, pose):
        if pose == libmyo.Pose.double_tap:
            myo.set_stream_emg(libmyo.StreamEmg.enabled)
            self.emg_enabled = True
        elif pose == libmyo.Pose.fingers_spread:
            myo.set_stream_emg(libmyo.StreamEmg.disabled)
            self.emg_enabled = False
            self.emg = None
        self.pose = pose
        if self.pose == "double_tap":
            myo.vibrate("short")
        self.output()

    def on_orientation_data(self, myo, timestamp, orientation):
        self.orientation = orientation
        self.output()

    def on_accelerometor_data(self, myo, timestamp, acceleration):
        pass

    def on_gyroscope_data(self, myo, timestamp, gyroscope):
        pass

    def on_emg_data(self, myo, timestamp, emg):
        self.emg = emg
        self.output()

    def on_unlock(self, myo, timestamp):
        self.locked = False
        self.output()

    def on_lock(self, myo, timestamp):
        self.locked = True
        self.output()

    def on_event(self, kind, event):
        """
        Called before any of the event callbacks.
        """

    def on_event_finished(self, kind, event):
        """
        Called after the respective event callbacks have been
        invoked. This method is *always* triggered, even if one of
        the callbacks requested the stop of the Hub.
        """

    def on_pair(self, myo, timestamp, firmware_version):
        """
        Called when a Myo armband is paired.
        """

    def on_unpair(self, myo, timestamp):
        """
        Called when a Myo armband is unpaired.
        """

    def on_disconnect(self, myo, timestamp):
        """
        Called when a Myo is disconnected.
        """

    def on_arm_sync(self, myo, timestamp, arm, x_direction, rotation,
                    warmup_state):
        """
        Called when a Myo armband and an arm is synced.
        """

    def on_arm_unsync(self, myo, timestamp):
        """
        Called when a Myo armband and an arm is unsynced.
        """

    def on_battery_level_received(self, myo, timestamp, level):
        """
        Called when the requested battery level received.
        """

    def on_warmup_completed(self, myo, timestamp, warmup_result):
        """
        Called when the warmup completed.
        """


def main():
    print("Connecting to Myo ... Use CTRL^C to exit.")
    try:
        hub = libmyo.Hub()
    except MemoryError:
        print("Myo Hub could not be created. Make sure Myo Connect is running.")
        return

    hub.set_locking_policy(libmyo.LockingPolicy.none)
    hub.run(1000, Listener())

    # Listen to keyboard interrupts and stop the hub in that case.
    try:
        while hub.running:
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("\nQuitting ...")
    finally:
        print("Shutting down hub...")
        hub.shutdown()


if __name__ == '__main__':
    main()