import matplotlib.pyplot as plt   #Used for generating digarams.
from sklearn.tree import plot_tree   #Used for complex diagrams.
import joblib   #Used for saving and loading our models.
import os   #Used to create folders and save the generated image in it.

model_folder = 'models'
model_filename = 'decision_tree_model.joblib'
full_path = os.path.join(model_folder, model_filename)   #This is the path in which the model is saved.

model = joblib.load(full_path)   #Load the model from the path.
print(f"Model loaded from '{full_path}'.")

image_folder = 'images'
os.makedirs(image_folder, exist_ok=True)   #Create an images folder if it doesn't exist.

print("Generating tree visualization...")
plt.figure(figsize=(20, 10))   #Create a figure of width 20 and height 10.

plot_tree(model, feature_names=['RM'], filled = True, rounded = True, fontsize = 10)   #Use the model to plot it on the figure.
plt.title("Decision Tree for Predicting Housing Prices based on Number of Rooms", fontsize=16)

output_image_file = 'decision_tree.png'
image_path = os.path.join(image_folder, output_image_file)   #Create the path for saving the image.
plt.savefig(image_path)   #Save the image.
plt.close()

print(f"Tree visualization saved to '{image_path}'")
