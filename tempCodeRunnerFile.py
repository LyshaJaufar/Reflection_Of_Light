                   pygame.draw.rect(self.display_canvas,
                                    color,
                                    [(self.margin + self.tile_size) * (abs(column-j))+self.margin,
                                    (self.margin + self.tile_size) * (abs(row-i))+self.margin,
                                    self.tile_size,
                                    self.tile_size])