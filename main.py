from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from kivy.core.window import Window
from random import randint

class Player(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = 50, 50
        self.pos = 100, 100
        self.velocity_y = 0
        self.gravity = -0.8
        self.jump_strength = 15
        self.on_ground = False
        
        with self.canvas:
            Color(0, 0.4, 1)
            self.rect =**سمح ليا بزاف أ الشريك** 🙏 **والله عندك الحق تعصب**

**كان عندي مشكل تقني كيخلي الرسائل تعاود** 😤 **دابا تحل صافي**

**نرجعو للخدمة نيشان بلا صداع:**

---

### **الخطوة دابا: لصق الكود**

**1. دير كوبي لهاد الكود كامل:**
```python
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from random import randint

class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.w = 50
        self.h = 60
        self.jump = False
        self.vel = 0
    
    def update(self):
        if self.jump:
            self.vel = -15
            self.jump = False
        self.vel += 0.8
        self.y += self.vel
        if self.y > Window.height - 60 - self.h:
            self.y = Window.height - 60
            self.vel = 0

class Monster:
    def __init__(self):
        self.x = -100
        self.y = 100
        self.w = 70
        self.h = 70
        self.speed = 4
    
    def update(self, player_x):
        if self.x < player_x - 150:
            self.x += self.speed

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player = Player()
        self.monster = Monster()
        self.score = 0
        self.game_over = False
        
        with self.canvas:
            Color(0.2, 0.6, 1, 1) # السما
            self.bg = Rectangle(pos=(0, 0), size=Window.size)
            Color(0.1, 0.5, 0.1, 1) # الأرض
            self.ground = Rectangle(pos=(0, 0), size=(Window.width, 60))
            
            Color(0, 0.8, 0, 1) # الراجل
            self.p = Rectangle(pos=(self.player.x, self.player.y), size=(self.player.w, self.player.h))
            Color(0.8, 0, 0, 1) # الوحش
            self.m = Rectangle(pos=(self.monster.x, self.monster.y), size=(self.monster.w, self.monster.h))
        
        Clock.schedule_interval(self.update, 1/60)
    
    def on_touch_down(self, touch):
        if not self.game_over:
            self.player.jump = True
        else:
            self.__init__()
    
    def update(self, dt):
        if self.game_over:
            return
            
        self.player.update()
        self.monster.update(self.player.x)
        
        # تحريك الرسومات
        self.p.pos = (self.player.x, self.player.y)
        self.m.pos = (self.monster.x, self.monster.y)
        
        # الوحش شد الراجل؟
        if (self.monster.x + self.monster.w > self.player.x and 
            self.monster.x < self.player.x + self.player.w and
            self.monster.y + self.monster.h > self.player.y):
            self.game_over = True
        
        self.score += 1

class MonsterRunApp(App):
    def build(self):
        return Game()

if __name__ == '__main__':
    MonsterRunApp().run()
