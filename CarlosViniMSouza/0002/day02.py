# The get() method on dicts and its "default" argument

names = {
    382: "Beatriz",
    590: "Carlos",
    951: "Dilbert",
}


def greeting(userid):
    return "Hi %s!" % names.get(userid, "there")


print(greeting(382))
# Output: "Hi Alice!"

print(greeting(333))
# Output: "Hi there!"

print(greeting(951))
# Output: "Hi Dilbert!"
