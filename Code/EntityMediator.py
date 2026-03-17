class EntityMediator:

    @staticmethod
    def verify_collision(entity_list):

        remove_list = []

        for i in range(len(entity_list)):
            ent1 = entity_list[i]

            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]

                #  PLAYER vs ENEMY
                if ent1.name == "Player1" and ent2.name == "Enemy":

                    if ent1.rect.colliderect(ent2.rect):
                        ent1.life -= 1
                        remove_list.append(ent2)

                elif ent2.name == "Player1" and ent1.name == "Enemy":

                    if ent1.rect.colliderect(ent2.rect):
                        ent2.life -= 1
                        remove_list.append(ent1)

                #  TIRO vs ENEMY
                if ent1.name == "PlayerShot" and ent2.name == "Enemy":

                    if ent1.rect.colliderect(ent2.rect):
                        remove_list.append(ent1)
                        remove_list.append(ent2)

                elif ent2.name == "PlayerShot" and ent1.name == "Enemy":

                    if ent1.rect.colliderect(ent2.rect):
                        remove_list.append(ent1)
                        remove_list.append(ent2)

        # remove duplicados
        remove_list = list(set(remove_list))

        for ent in remove_list:
            if ent in entity_list:
                entity_list.remove(ent)