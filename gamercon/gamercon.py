import argparse
import asyncio
import sys
from gamercon_async import GameRCON

parser = argparse.ArgumentParser(description='GameRCON command executor.')
parser.add_argument('-H', '--host', required=True, help='Server host address')
parser.add_argument('-P', '--port', required=True, type=int, help='Server RCON port')
parser.add_argument('-p', '--password', required=True, help='Server RCON password')
parser.add_argument('-c', '--command', required=True, help='Command to execute on the server')
parser.add_argument('-v', '--version', action='version', version='GameRCON v0.1.3')
parser.add_argument('-t', '--timeout', type=int, default=10, help='Connection timeout in seconds (optional)')

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

async def main():
    try:
        async with GameRCON(args.host, args.port, args.password, args.timeout) as rcon:
            response = await rcon.send(args.command)
            print(response)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())