class EntityMediator:

    @staticmethod
    def verify_collision(entity_list):

        remove_list = []

        for ent1 in entity_list:
            for ent2 in entity_list:

                if ent1 == ent2:
                    continue

                # player vs enemy
                if ent1.name == "Player1" and ent2.name == "Enemy":

                    if ent1.rect.colliderect(ent2.rect):

                        ent1.life -= 1
                        remove_list.append(ent2)

                # tiro vs enemy
                if ent1.name == "PlayerShot" and ent2.name == "Enemy":

                    if ent1.rect.colliderect(ent2.rect):

                        remove_list.append(ent1)
                        remove_list.append(ent2)

        for ent in remove_list:

            if ent in entity_list:
                entity_list.remove(ent)