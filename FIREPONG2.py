from asyncio import sleep
import arcade
import random


#V1.1 de FIREPONG2 not fire tho
# 
#Juego de pong con powerups
#No tocar las cosas comentadas(actualizaciones futuras)
#Power de la V1.1 (Cada que tenga 5 puntos puede mover al jugador y se le cobrara 5 puntos del score)
#Version juego infinito.





# Dimensiones de la ventana


ANCHO_VENTANA = 800
ALTO_VENTANA = 600
VELOCIDAD_BOLA=7    
VELOCIDAD_PLAYER1=7
VELOCIDAD_PLAYER2=7
radius=10
#BULLET_SPEED=20
class JuegoPong(arcade.Window):
    def __init__(self):
        super().__init__(ANCHO_VENTANA, ALTO_VENTANA, "Pong")

      
        #self.bullet_list = arcade.SpriteList()
        self.sprites= arcade.SpriteList()
        self.enemies = arcade.SpriteList()
        
        self.scorejugador1 = 0
        self.scorejugador2 = 0
        self.scoremonedas1= 0
        self.scoremonedas2 =0
        self.texto="Make a point | Kill a boi :)"
        self.texto1="Press SPACE c;;"
        self.texto2="Press LEFT c;"

        
        self.player1 = arcade.SpriteSolidColor(10, 70, arcade.color.WHITE)
       # self.player1.velocity=(0,250)
        self.player1_x = 20
        self.player1_y = ALTO_VENTANA // 2 
        self.player1change=0

        self.sprites.append(self.player1)


        self.player2 = arcade.SpriteSolidColor(10, 70, arcade.color.WHITE)
        #self.player2.velocity=(0,250)
        self.player2_x = ANCHO_VENTANA - 20
        self.player2_y = ALTO_VENTANA // 2
        self.player2change=0

        self.sprites.append(self.player2)

        self.Bola =arcade.SpriteSolidColor(radius * 2, radius *2 ,arcade.color.WHITE)
        self.BolaX= ANCHO_VENTANA /2
        self.BolaY= ALTO_VENTANA /2 
        self.VelocidadBolaX= VELOCIDAD_BOLA 
        self.VelocidadBolaY= VELOCIDAD_BOLA 

        #self.shoot_direction = "right"
        

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f'{self.scorejugador1} | {self.scorejugador2}', ANCHO_VENTANA/2.1,ALTO_VENTANA-50,arcade.csscolor.WHITE)
        arcade.draw_text(f'{self.texto}', ANCHO_VENTANA/2.7,ALTO_VENTANA-30,arcade.csscolor.WHITE)
        self.player1.center_x = self.player1_x
        self.player1.center_y = self.player1_y
      
        if self.scorejugador1 -5 != -1 and self.scorejugador1>=5:
            arcade.draw_text(f'{self.texto1}', ANCHO_VENTANA/7,ALTO_VENTANA-500,arcade.csscolor.WHITE)

        if self.scorejugador2 -5 != -1 and self.scorejugador2>=5:
            arcade.draw_text(f'{self.texto2}', ANCHO_VENTANA-300,ALTO_VENTANA-500,arcade.csscolor.WHITE)


        arcade.draw_text(
            f"Score: {self.scorejugador2}",
            700,
            35,
            arcade.color.YELLOW,
            15,
            width=ANCHO_VENTANA,
            align="left"
        )
        
        arcade.draw_text(
            f"Score: {self.scorejugador1}",
            20,
            35,
            arcade.color.YELLOW,
            15,
            width=ANCHO_VENTANA,
            align="left"
        )
        #self.player1.draw()

        self.player2.center_x = self.player2_x
        self.player2.center_y = self.player2_y
        self.sprites.draw()
       # self.bullet_list.draw()
       # self.player2.draw()
        
        self.Bola.center_x = self.BolaX
        self.Bola.center_y = self.BolaY
        self.Bola.draw()

       # self.bullet_list.draw()
    def update(self, delta_time):

        #self.update_enemies()
        self.sprites.update()
        #self.update_bullets1()

        if arcade.check_for_collision(self.Bola,self.player1) or arcade.check_for_collision(self.Bola,self.player2):
            self.VelocidadBolaX*= -1
            self.VelocidadBolaY+= random.uniform(-1,1)

        self.player1_y+= self.player1change
        self.player2_y+= self.player2change

        self.BolaX += self.VelocidadBolaX
        self.BolaY += self.VelocidadBolaY

 
        if self.BolaX<10:
            self.scorejugador2 +=1 
            sleep(1)
            self.BolaX= ANCHO_VENTANA /2
            self.BolaY= ALTO_VENTANA /2 
            self.VelocidadBolaX *=-1
            print (self.scorejugador2)   

        if self.BolaX> ANCHO_VENTANA - 20:
            self.scorejugador1 +=1 
            sleep(1)
            self.BolaX= ANCHO_VENTANA /2
            self.BolaY= ALTO_VENTANA /2 
            self.VelocidadBolaX *=-1
        if self.BolaY<10 or self.BolaY >ALTO_VENTANA -10:
            self.VelocidadBolaY *= -1
        

        if self.player1_y<50:
            self.player1_y+=VELOCIDAD_PLAYER1
        if self.player1_y>ALTO_VENTANA - 50:
            self.player1_y-=VELOCIDAD_PLAYER1
              
        if self.player2_y<50:
            self.player2_y+=VELOCIDAD_PLAYER2
        if self.player2_y>ALTO_VENTANA - 50:
            self.player2_y-=VELOCIDAD_PLAYER2

      #  self.bullet_list.update()
        #for  bullet in self.bullet_list:
            #hit_list = arcade.check_for_collision_with_list(bullet )
    #def update_bullets1(self):
      #  for b in self.bullet_list:
          #  if b.top > self.player1.center_y + ALTO_VENTANA or b.bottom < 0 or b.left < -self.player1.center_x or b.right > self.player1.center_x + ANCHO_VENTANA:
             #   print(f"Log Bala: Punto x= {self.player1.center_x}, Punto_y = {self.player1.center_y}")
               # b.remove_from_sprite_lists()

  #  def update_enemies(self):
        #for e in self.enemies:
            #if e.collides_with_list(self.Bola):
             #   e.remove_from_sprite_lists()
                #self.scoremodedas1 += 1

   # def add_enemy(self, delta_time):
       # enemy = arcade.SpriteSolidColor(30, 30, arcade.color.RED)
        #enemy.left = random.randint(10, ALTO_VENTANA- 10)
        #enemy.top = random.randint(10, ANCHO_VENTANA - 10)
        #self.enemies.append(enemy)
        #self.sprites.append(enemy)

    def on_key_press(self, symbol, modifiers):
       
        #Jugador uno
        if symbol == arcade.key.W:
            self.player1change = VELOCIDAD_PLAYER1
        if symbol == arcade.key.S:
            self.player1change = -VELOCIDAD_PLAYER1
        if symbol == arcade.key.SPACE:
            print(f"Score:{ self.scorejugador1}" )
            if self.scorejugador1-5 != -1 and self.scorejugador1>=5:
                 self.player2_y-=250
                 self.scorejugador1-=5
               

           #Jugador dos
        if symbol == arcade.key.UP:
            self.player2change = VELOCIDAD_PLAYER2
        if symbol == arcade.key.DOWN:
            self.player2change = -VELOCIDAD_PLAYER2
        if symbol == arcade.key.LEFT: 
            if self.scorejugador2-5 != -1 and self.scorejugador2>=5:
                self.player1_y-=250
                self.scorejugador2-=5
        
                
                
       
        

     #   if symbol == arcade.key.SPACE:
          #  bullet = arcade.Sprite("sprites/bullet.png")
          #  bullet.scale=0.5
          #  bullet.center_X = self.player1.center_x
          #  bullet.center_Y = self.player1.center_y -10
            
           # if self.shoot_direction == "right":
             #   bullet.velocity(BULLET_SPEED,0)
           # else:
              # bullet.velocity(-BULLET_SPEED,0)
  
           # self.bullet_list.append(bullet)

      

         
    def on_key_release(self, symbol, modifiers ):
       
        #Jugador uno
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.player1change=0
        
          
         #Jugador dos
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player2change=0
 
            
       


        
def main():
    ventana = JuegoPong()
    arcade.run()


if __name__ == "__main__":
    main()