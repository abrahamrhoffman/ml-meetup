# Phoenix ML
<h3>MNIST Part 2</h3>
Install Requirements:

```
pip install tensorflow pandas numpy matplotlib
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
cd ..
```

Now you should understand how to obtain, extract, convert and split the MNIST database.

<h4>MNIST Dataset Simple Visualization</h4>

```
# Above, we converted binary to row vectors and row vectors to CSV.
# Let's visualize one of the images
python mnist-visualize-digits.py
# Pretty cool right? Remove the "break" at the end of the file to see view all reconstructed digits

# Now, let's import one of the CSVs into python and convert it into a pandas Data Frame
python mnist-dataframe-example.py
...
# Look through the output and the "mnist-dataframe-example.py' file for some intuition on what's happening.
```

<h4>Our First MNIST Neural Network</h4>

```
# Now we're ready to run our first mnist neural network
python our-first-mnist-nn.py
```

After a bit, you should see output like this:

```
Successfully downloaded train-images-idx3-ubyte.gz 9912422 bytes.
Extracting MNIST_data/train-images-idx3-ubyte.gz
Successfully downloaded train-labels-idx1-ubyte.gz 28881 bytes.
Extracting MNIST_data/train-labels-idx1-ubyte.gz
Successfully downloaded t10k-images-idx3-ubyte.gz 1648877 bytes.
Extracting MNIST_data/t10k-images-idx3-ubyte.gz
Successfully downloaded t10k-labels-idx1-ubyte.gz 4542 bytes.
Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
Training Step:0  Accuracy =  0.6668  Loss = 2.19803
Training Step:100  Accuracy =  0.8724  Loss = 0.617316
Training Step:200  Accuracy =  0.8861  Loss = 0.498552
Training Step:300  Accuracy =  0.8941  Loss = 0.449356
Training Step:400  Accuracy =  0.8989  Loss = 0.4209
Training Step:500  Accuracy =  0.9019  Loss = 0.40177
Training Step:600  Accuracy =  0.905  Loss = 0.387756
Training Step:700  Accuracy =  0.9074  Loss = 0.376902
Training Step:800  Accuracy =  0.909  Loss = 0.368162
Training Step:900  Accuracy =  0.9103  Loss = 0.360921
Training Step:1000  Accuracy =  0.9119  Loss = 0.354787
Training Step:1100  Accuracy =  0.9125  Loss = 0.3495
Training Step:1200  Accuracy =  0.9136  Loss = 0.344879
Training Step:1300  Accuracy =  0.9142  Loss = 0.340792
Training Step:1400  Accuracy =  0.9146  Loss = 0.337143
Training Step:1500  Accuracy =  0.9152  Loss = 0.333857
Training Step:1600  Accuracy =  0.9156  Loss = 0.330877
Training Step:1700  Accuracy =  0.9159  Loss = 0.328157
Training Step:1800  Accuracy =  0.9162  Loss = 0.32566
Training Step:1900  Accuracy =  0.917  Loss = 0.323358
Training Step:2000  Accuracy =  0.9172  Loss = 0.321226
Training Step:2100  Accuracy =  0.9172  Loss = 0.319243
Training Step:2200  Accuracy =  0.9171  Loss = 0.317393
Training Step:2300  Accuracy =  0.9175  Loss = 0.315661
Training Step:2400  Accuracy =  0.9176  Loss = 0.314034
Training Step:2500  Accuracy =  0.918  Loss = 0.312503
```
