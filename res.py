import websockets
import asyncio
import check as check

SessionID = "molodoy_petrovich"

width = 100
type = "L1"
amount = 10
per = 3


async def work2():
    url = "wss://sprs.herokuapp.com/second/" + SessionID
    async with websockets.connect(url) as websocket:
        req = (f"Let's start with {width} {type} {amount} {per}")
        await websocket.send(req)
        resp = await websocket.recv()
        print(f"\n>Request: {req} \n<Response: {resp}")
        for step in range(1, amount + 1):
            req = ("Ready")
            await websocket.send(req)
            resp = await websocket.recv()
            print(f"\n>Request: {req} \n<Response: {resp}")
            x = check.Normalize(check.Parse(resp))
            if (type == "L1"):
                answer = str(check.rec1(x))
            else:
                answer = str(check.rec2(x, int(type)))
            a = answer + " "
            req = (f"{step}\n{a*(per-1)}{answer}")
            await websocket.send(req)
            resp = await websocket.recv()
            print(f"\n{req} \n{resp}")

        req = ("Bye")
        await websocket.send(req)
        resp = await websocket.recv()
        print(f"\n{req} \n{resp}")

        input("Press enter")


asyncio.get_event_loop().run_until_complete(work2())
