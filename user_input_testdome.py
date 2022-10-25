class TextInput:
    def __init__(self):
      self.value = ""
     
    def add(self, ch):
      self.value += ch
      
    def get_value(self):
      return self.value
  
class NumericInput(TextInput):
    def add(self,ch):
      if ch.isnumeric():
        self.value += ch
      

if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())