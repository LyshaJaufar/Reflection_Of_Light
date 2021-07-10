            for ray in self.incidentRays:
                ray.draw(window)
                for ray in self.reflectedRays:
                    ray.draw(window)