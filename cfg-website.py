class Webpage:
    def __init__(self, name, slug, parent_page=None):
        self.name = name
        self.slug = slug
        self.child_pages = []
        self.parent_page = parent_page
        if parent_page:
            parent_page.add_child_page(self)
    
    def add_child_page(self, child_page):
        self.child_pages.append(child_page)

    def page_link(self):
        return f"https://codefirstgirls.com{self.slug}"
    
    def options(self):
        child_names = [child_page.name for child_page in self.child_pages]
        if self.parent_page:
            return ", ".join(child_names + ["Back"])
        return ", ".join(child_names)

    def output_message(self):
        print(f"You are on the {self.name} page at URL: {self.page_link()}")

    def navigate(self):
        option = input(f"Where are you clicking?\nOptions: {self.options()}\n").lower().strip()
        if option in ["q", "quit", "e", "exit"]:
            return False
        if option == "back" and self.parent_page:
            return self.parent_page
        for child_page in self.child_pages:
            if option == child_page.name.lower():
                return child_page
        print(f"\nInvalid option {option}\n")
        return self

homepage = Webpage("Homepage", "/")
courses = Webpage("View Courses", "/courses", homepage)
cfg_degree = Webpage("CFG Degree", "/cfgdegree", courses)
opportunities = Webpage("Opportunities", "/opportunities", homepage)
ambassador = Webpage("Become an Ambassador", "/ambassador", opportunities)

# @Navigator
def cfg_website(current_page):
    while current_page:
        current_page.output_message()
        current_page = current_page.navigate()
    print("Goodbye!")

cfg_website(homepage)