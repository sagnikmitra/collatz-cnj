from treelib import Node, Tree
tree = Tree()
tree.create_node("1", 1)
addedNums = []
def operate(num):
      if(num % 2 == 0):
          return num // 2
      else:
          return num * 3 + 1
def run_through(num):
      chain = [num]
      while(num != 1):
            num = operate(num)
            chain.insert(0, num) 
      for i in range(1, len(chain)): 
          if not chain[i] in addedNums:
              tree.create_node(str(chain[i]), chain[i], parent = chain[i-1])
               addedNums.append(chain[i])