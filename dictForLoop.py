def find_kittens(dict_arg):
  kittens = []
  for k, v in dict_arg.items():
    if v == 'kitten':
      kittens.append(k)
  return kittens
