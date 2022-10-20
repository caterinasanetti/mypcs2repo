def mutate_string(string, position, character):
  l = list(string)
  l[position] = character
  mutated=''.join(l)
  return mutated  