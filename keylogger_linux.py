import pyxhook

#this function is called everytime a key is pressed.
def OnKeyPress(event):
  print(event.Key)

  if event.Ascii==96: #96 is the ascii value of the grave key (`)
    fob.close()
    new_hook.cancel()
new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
