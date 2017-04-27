import random
import tkinter as tk
import pygame

class remote(object):
    def __init__(self, laptop):
        self.laptop= laptop
        self.on = False
    def click(self):
        if not self.on:
            self.laptop.on()
            self.on = True
    def close(self):
        if self.on:
            self.laptop.title1.destroy()
            self.laptop.title2.destroy()
            self.laptop.button.destroy()
            self.laptop.entry.destroy()
            self.on = False


class laptop(tk.Tk):
    def __init__(self, key):
        
        self.game = dict()
        self.game['scar'] = {'display':'s _ _ r', 'definition':'a mark \
left on the skin or within body tissue where a wound, burn, or sore has \
not healed completely and fibrous connective tissue has developed.'}
        self.key = key
        self.puzzle_finish = False
        tk.Tk.__init__(self)
        '''
	self.game['escape'] = {'display':'_ s _ _ _ e', 'definition':'break \
	free from confinement or control'}

	self.game['convenience'] = {'display':'c _ n _ _ _ _ e _ _ _', \
	'definition':'the state of being able to proceed with \
	omething with little effort or difficulty'}
	'''

    def on(self):
        
        self.entry = tk.Entry(self)
        self.title1 = tk.Label(text = self.game['scar']['definition'])
        self.title2 = tk.Label(text = self.game['scar']['display'])
        self.button = tk.Button(self, text="I want to answer!", command=self.answer)
        self.title1.pack()
        self.title2.pack()
        self.entry.pack()
        self.button.pack()

    def answer(self):
        result = self.entry.get()
        if (result != 'scar'):
            print("wrong answer!")
        else:
            if not self.puzzle_finish: 
                print("key got")
                self.key.key_got()
                self.puzzle_finish = True
            self.title1.destroy()
            self.title2.destroy()
            self.button.destroy()
            self.entry.destroy()
        return "you solve it!"
            self.
            
class key(object):
    def __init__(self):
        self.complete = False
        self.sum = 0

    def key_got(self):
        self.sum += 1

    def finish(self):
        return self.sum >= 3




