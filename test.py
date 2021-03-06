#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from pprint import pprint

def drawCarpet(locx, locy, locz, size, blockId, blockData):
    mc.setBlocks(locx + 1, locy, locz + 1, locx + size, locy, locz + size, blockId, blockData)


if __name__ == "__main__":
    pprint(block.END_PORTAL.__dict__, indent=2)
    mc = minecraft.Minecraft.create()
    orig = mc.player.getTilePos()
    drawCarpet( orig.x, orig.y, orig.z, 3, block.CARPET_ORANGE.id, block.CARPET_ORANGE.data)

    while True:
        time.sleep(2)
        pos = mc.player.getTilePos()
        if pos.x > orig.x and pos.x < orig.x + 3 + 1 and pos.z > orig.z and pos.z < orig.z + 3 + 1:
            print("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))
            mc.postToChat("Welcome to the orange carpet!")
