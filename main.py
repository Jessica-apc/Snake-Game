import pygame

print("Setup Start") # Start = inicio
pygame.init()
window = pygame.display.set_mode( size= (600, 480))
print("Setup End") # End = Fim

print("Loop Start")
while True :
     # Check for all events "Cheque por todos os eventos"
     for event in pygame.event.get():
        if event .type == pygame.QUIT:
           pygame.quit() # Close window = Fechar janela
           quit()



