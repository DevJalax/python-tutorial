items = [];

for i in range(1, len(lines)):
	
	line = lines[i].split(', ');

	itemFeatures = {"Class" : line[-1]};

	# Iterate through the features
	for j in range(len(features)):
	
		# Get the feature at index j
		f = features[j];
			
		# The first item in the line
		# is the class, skip it
		v = float(line[j]);
		
		# Add feature to dict
		itemFeatures[f] = v;
	
	# Append temp dict to items
	items.append(itemFeatures);
	
shuffle(items);

def Classify(nItem, k, Items):
	if(k > len(Items)):
		
		# k is larger than list
		# length, abort
		return "k larger than list length";
	
	# Hold nearest neighbors.
	# First item is distance,
	# second class
	neighbors = [];

	for item in Items:
	
		# Find Euclidean Distance
		distance = EuclideanDistance(nItem, item);

		# Update neighbors, either adding
		# the current item in neighbors
		# or not.
		neighbors = UpdateNeighbors(neighbors, item, distance, k);

	# Count the number of each
	# class in neighbors
	count = CalculateNeighborsClass(neighbors, k);

	# Find the max in count, aka the
	# class with the most appearances.
	return FindMax(count);

def EuclideanDistance(x, y):
	
	# The sum of the squared
	# differences of the elements
	S = 0;
	
	for key in x.keys():
		S += math.pow(x[key]-y[key], 2);

	# The square root of the sum
	return math.sqrt(S);

def UpdateNeighbors(neighbors, item, distance, k):
	
	if(len(neighbors) > distance):
			
			# If yes, replace the last
			# element with new item
			neighbors[-1] = [distance, item["Class"]];
			neighbors = sorted(neighbors);

	return neighbors;

def CalculateNeighborsClass(neighbors, k):
	count = {};
	
	for i in range(k):
		
		if(neighbors[i][1] not in count):
		
			# The class at the ith index
			# is not in the count dict.
			# Initialize it to 1.
			count[neighbors[i][1]] = 1;
		else:
			
			# Found another item of class
			# c[i]. Increment its counter.
			count[neighbors[i][1]] += 1;

	return count;

def FindMax(countList):
	
	# Hold the max
	maximum = -1;
	
	# Hold the classification
	classification = "";
	
	for key in countList.keys():
	
		if(countList[key] > maximum):
			maximum = countList[key];
			classification = key;

	return classification, maximum;
