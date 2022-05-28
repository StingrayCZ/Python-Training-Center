from faker import Faker

fake = Faker()

print(fake.name())
print(f"{fake.address()}\n")


for a in range(10):
  print(fake.ipv4_private())