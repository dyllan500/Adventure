import pytmx
import pygame as pg

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface, remove):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if remove is True:
                        if tile and layer.name != 'straw':
                            surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))
                    else:
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

    def make_map(self, remove):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface, remove)
        return temp_surface
