def word_histogram(paragraph):
  histogram = {}
  word_list = paragraph.split()
  for word in word_list:
    if word in histogram:
      histogram[word] = histogram[word] + 1
    else:
      histogram[word] = 1
  sorted_histogram = sorted(histogram, key=lambda word:word[1])
  print(sorted_histogram)
  return sorted_histogram[:3]

print(word_histogram('To be or not to be do be do be do'))