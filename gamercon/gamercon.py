import argparse
import asyncio
from gamercon_async import GameRCON

# Command line parsing
parser = argparse.ArgumentParser(description='GameRCON command executor.')
parser.add_argument('-host', required=True, help='Server host address')
parser.add_argument('-port', required=True, type=int, help='Server port')
parser.add_argument('-pass', dest='password', required=True, help='RCON password')
parser.add_argument('-command', required=True, help='Command to execute on the server')
args = parser.parse_args()

# Sends command to game server
async def main():
    async with GameRCON(args.host, args.port, args.password, timeout=10) as rcon:
        response = await rcon.send(args.command)
        print(response)

# Entry point
if __name__ == "__main__":
    asyncio.run(main())
