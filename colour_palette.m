% Step 1: Load the image
imgPath = fullfile('apod', 'apod.jpg');

if ~isfile(imgPath)
    error('File not found: %s', imgPath);
end

img = imread(imgPath);

% Step 2: Resize image for faster processing
imgResized = imresize(img, 0.1);

% Step 3: Reshape image data for clustering
imgData = double(reshape(imgResized, [], 3));

% Step 4: Perform k-means clustering
numColours = 5;  % Define number of palette colour
[idx, palette] = kmeans(imgData, numColours, 'MaxIter', 500, 'Replicates', 3);

% Step 5: Display the original image
subplot(1, 2, 1);
imshow(img);
title('Astronomy Picture of the Day (APOD)');

% Step 6: Display the extracted colour palette
subplot(1, 2, 2);
paletteImage = reshape(palette, 1, [], 3) / 255; % Normalize to [0,1]
imshow(paletteImage);
title('APOD Colour Palette');
