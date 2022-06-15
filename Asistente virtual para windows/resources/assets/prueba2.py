import pyglet
 
animation = pyglet.image.load_animation('2.gif')
animSprite = pyglet.sprite.Sprite(animation,x=-30,y=60)
 
animSprite.scale_x = 0.3
animSprite.scale_y = 0.3
 
w = animSprite.width
h = animSprite.height
 
window = pyglet.window.Window(width=w, height=h)
 
#r,g,b,alpha = 0.5,0.5,0.8,0.5
 
 
#pyglet.gl.glClearColor(r,g,b,alpha)
 
@window.event
def on_draw():

    window.clear()
    animSprite.draw()
pyglet.app.overrideredirect(True) 
 
 
pyglet.app.run()


