def cat_dog(s):
    cat_count = s.count("cat")
    dog_count = s.count("dog")

    if cat_count==dog_count:
        return True
    else:
        return False    



tap = cat_dog("catcatapdog")
print(tap)