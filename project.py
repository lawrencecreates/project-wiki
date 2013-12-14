u"""
Project list
"""

import csv
from jinja2 import Environment
from jinja2 import PackageLoader

class Field(object) :
    def __init__(self, name):
        self.name = name

class Text(Field) :
    def __init__(self, name, descr=""):
        Field.__init__(self,name)
        self.descr= descr

class Select(Text) :
    def __init__(self, name, descr, item_list):
        Text.__init__(self,name, descr)
        self.items_list = item_list

class Project :    
    def __init__(self, values):
        self.developer=values[0]  #Text("Project Developer","(your name)")
        self.title=values[1]      # Text("Project Title")

        self.contact  = values[2] #Text("Project Developer Contact Information",
        #"(email and phone number -- let us know your preferred method of contact)")

        self.team = values[3]     # Select("Lab/Team","(e.g. HackLab):",["Woodshop","Hacklab","Art Center","3d printing"])
        self.members  = values[4] # Text("Team Members")
        self.summary  = values[5] # Text("Summary")
        self.timeline = values[6] # Text("Timeline/Deadlines")
        self.resources = values[7] # Text("Resources Needed")
        self.vision = values[8] #Text("Final vision","how the project relates to the mission of Lawrence Creates")
        self.links = values[9] #Text("Any other relevant information or links")

    def write_markdown(self):
        u'''
        re
        '''
        loader = PackageLoader("project","templates")
        env = Environment(loader=loader)
        template_file ="project.tpl"
        # print template_file
        template = env.get_template(template_file)
        # Finally, process the template to produce our final text.
        html = template.render(self.__dict__)


        with open("projects/%s.md" % self.title , 'w') as outfile:
            outfile.write(html)

class Projects :
    def __init__(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                #Timestamp, 
                #Project Title, 
                #Project Developer, 
                #Project Developer Contact Information,  
                #Lab/Team, 
                #Team Members, 
                #Summary, 
                #Timeline/Deadlines, 
                #Resources Needed, 
                #Final vision & how the project relates to the mission of Lawrence Creates, 
                #Any other relevant information or links
                #print (', '.join(row))
                p = Project(row)
                p.write_markdown()


if __name__ == "__main__":
    p = Projects("data.csv")
