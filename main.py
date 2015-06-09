from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class jprob(GridLayout):

    def __init__(self, **kwargs):
        super(jprob, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='N'))
        self.N = TextInput(multiline=False)
        self.add_widget(self.N)
        self.add_widget(Label(text='skip'))
        self.skip = TextInput(multiline=False)
        self.add_widget(self.skip)

        self.add_widget(Button(text="Solve Joeseph's Problem"))
        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)
        self.add_widget(cb)
        self.output = Button(text='Hello 1', size_hint_x=None, width=100)
        self.add_widget(self.output)

    def btn_pressed(self, instance, pos):
        print ('pos: printed from root widget: {pos}'.format(pos=pos))
        print ('Abra ka Dabra')
        self.output.text=self.evaluate()

    def evaluate(self):
        n= getint(self.N.text)
        #n=int(str(self.N.text))
        if not n:
           print "Enter a proper Integer Value for 'N'"
           return "Enter a proper Integer Value for 'N'"
        skip=getint(self.skip.text)
        if not skip:
           print "Enter a proper Integer Value for 'SKIP'"
           return "Enter a proper Integer Value for 'SKIP'"        
        
        people=[]
        kill_list=[]
        for i in range(1,n+1):
            people.append(i)
        index=0
        while (len(people)>1):
              index=(index+skip)
              if (index>len(people)):
                  index = index % len(people)
              kill_list.append(people[index-1])
              people.remove(people[index-1])
              index=index-1
              if index<0:
                 index=0
              if index>len(people):
                 index=index % len(people)
              if len(kill_list)%10000 ==0:
                 print "Killed " + str(len(kill_list))
        print (str(people[0]))
        return str(people[0])     
        
def getint(x):
        try:
	    x =int(x)
        except TypeError:
            return False
        except ValueError:
            return False
        return x 


class CustomBtn(Widget):

     pressed = ListProperty([0, 0])

     def on_touch_down(self, touch):
         if self.collide_point(*touch.pos):
             self.pressed = touch.pos
             # we consumed the touch. return False here to propagate
             # the touch further to the children.
             return True
         return super(CustomBtn, self).on_touch_down(touch)

     def on_pressed(self, instance, pos):
         print ('pressed at {pos}'.format(pos=pos))

class MyApp(App):

    def build(self):
        return jprob()

if __name__ == '__main__':
    MyApp().run()
