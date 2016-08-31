#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# block.END_PORTAL.id
# block.CARPET_ORANGE.id

blockId = block.CARPET_ORANGE.id
blockData = block.CARPET_ORANGE.data

def drawCarpet(locx, locy, locz, size, blockId, blockData):
    mc.setBlocks(locx + 1, locy, locz + 1, locx + size, locy, locz + size, blockId, blockData)


if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    orig = mc.player.getTilePos()
    drawCarpet( orig.x, orig.y, orig.z, 3, blockId, blockData)

    while True:
        time.sleep(2)
        pos = mc.player.getTilePos()
        if pos.x > orig.x and pos.x < orig.x + 3 + 1 and pos.z > orig.z and pos.z < orig.z + 3 + 1:
            print("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))
            mc.postToChat("Welcome to the orange carpet!")
