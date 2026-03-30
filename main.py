from encode import hide_image
from decode import extract_image

# Hide image
hide_image('cover.jpg', 'secret.jpg', 'hidden.png')

# Extract image
extract_image('hidden.png', 'extracted.png')