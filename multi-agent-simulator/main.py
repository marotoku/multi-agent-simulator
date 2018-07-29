import sys
import os
import yaml
import Simulator

def main():
    fileName = sys.argv[1]
    with open(fileName, 'r') as f:
        params = yaml.load(f)
    simulator = Simulator.Simulator(params)
    simulator.run(52)

if __name__ == '__main__':
    main()