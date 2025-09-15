class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hi, I'm {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")

    def show_stack(self):
        print("My tech stack includes:")
        for i, tech in enumerate(self.tech_stack, 1):
            print(f"{i}. {tech}")

    def github_link(self):
        return f"https://github.com/{self.github_username}"


# Create my profile
my_profile = Profile(
    name="Sewankambo Elvis",
    favorite_language="Python",
    hobby="playing football and coding",
    tech_stack=["Python", "C++", "Git", "JavaScript", "React", "Node.js"],
    github_username="SewaElvis",
    fun_fact="The Code Wisperer"
)

# Call the methods
my_profile.introduce()
print()
my_profile.show_stack()
print(f"\nGitHub: {my_profile.github_link()}")  # Fixed this line
print(f"Fun fact: {my_profile.fun_fact}")