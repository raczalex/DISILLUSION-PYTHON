import subprocess
from utilities import print

class Fortnite():
    def __init__(self) -> None:
        pass

    def _pingHost(self,host="google.com", count=10):
        try:
            result = subprocess.run(['ping', host, '-n', str(count)], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.output

    def _parsePingOutput(self,output):
        lines = output.split('\n')
        stats_line = None
        for line in lines:
            if "Minimum" in line and "Maximum" in line and "Average" in line:
                stats_line = line
                break

        if stats_line:
            parts = stats_line.split(',')
            minimum = int(parts[0].split('=')[1].strip().replace('ms', ''))
            maximum = int(parts[1].split('=')[1].strip().replace('ms', ''))
            average = int(parts[2].split('=')[1].strip().replace('ms', ''))
            return minimum, maximum, average
        else:
            return None

    def _runPing(self,host,count):
        ping_output = self._pingHost(host, count)

        ping_stats = self._parsePingOutput(ping_output)

        if ping_stats:
            minimum, maximum, average = ping_stats
            print._printg('MINIMUM',f"{minimum}ms")
            print._printg('MAXIMUM',f"{maximum}ms")
            print._printg('AVERAGE',f"{average}ms\n")
        else:
            print._printr('FORTNITE','Failed to parse ping output.')

    def _europePingTest(self):
        self._runPing('ping-nae.ds.on.epicgames.com',10)

    def _naEastPingTest(self):
        self._runPing('ping-nae.ds.on.epicgames.com',10)

    def _naCentralPingTest(self):
        self._runPing('ping-nac.ds.on.epicgames.com',10)

    def _naWestPingTest(self):
        self._runPing('ping-naw.ds.on.epicgames.com',10)

    def _asiaPingTest(self):
        self._runPing('ping-asia.ds.on.epicgames.com',10)

    def _oceAustraliaPingTest(self):
        self._runPing('ping-oce.ds.on.epicgames.com',10)

    def _middleEastPingTest(self):
        self._runPing('ping-me.ds.on.epicgames.com',10)

    def _brazilPingTest(self):
        self._runPing('ping-br.ds.on.epicgames.com',10)

    def _doAll(self):
        print._printg('EUROPE','RESULTS')
        self._europePingTest()
        print._printg('NA EAST','RESULTS')
        self._naEastPingTest()
        print._printg('NA CENTRAL','RESULTS')
        self._naCentralPingTest()
        print._printg('NA WEST','RESULTS')
        self._naWestPingTest()
        print._printg('ASIA','RESULTS')
        self._asiaPingTest()
        print._printg('OCE / AUSTRALIA','RESULTS')
        self._oceAustraliaPingTest()
        print._printg('MIDDLE EAST','RESULTS')
        self._middleEastPingTest()
        print._printg('BRAZIL','RESULTS')
        self._brazilPingTest()
    
