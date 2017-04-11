# Phoenix ML
<h3>MNIST Part 2</h3>
Install Requirements:
```
pip install tensorflow pandas numpy
```

<h4>MNIST Dataset Manipulation</h4>

```
git clone https://github.com/abrahamrhoffman/MEETUP.git
cd MEETUP/MNIST-Neural-Network/part2

# A demonstration of how to download the MNIST dataset
bash mnist-data-prepare.sh
...
# Now, go into the folder that was just created
cd mnist

# Run the 'mnist-data-convert.py' script to convert the files into easy to read CSVs
python ../mnist-data-convert.py
# (Optional) Open the CSVs in Excel

# Split the CSVs into 'train.csv', 'validate.csv' and 'test.csv'
bash ../mnist-validate-create.sh
```

Now you should understand how to obtain, extract, convert and split the MNIST database.

<h4>MNIST Dataset Simple Visualization</h4>

```
# Above, we converted binary to row vectors and row vectors to CSV.
# Now, let's import the CSVs into 

```
