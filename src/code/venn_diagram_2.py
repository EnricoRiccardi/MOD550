# import modules 
from matplotlib_venn import venn2,venn2_circles 
from matplotlib import pyplot as plt 
  
# depict venn diagram 
venn2(subsets = (0, 3, 20), 
      set_labels = ('Group A', 'Group B'), 
      set_colors=("orange", "blue"),
      alpha=0.5)
  
# add outline 
venn2_circles(subsets=(0,3,20)
              linestyle="dashed",
              linewidth=2)  

# add descriptor
plt.title("Venn Diagram")   
plt.show()

