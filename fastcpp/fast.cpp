#include <iostream>
#include <opencv2/opencv.hpp>

// Find corners in an image.
cv::Mat fastDetect(const cv::Mat& image) {
    // Convert the original image to grayscale.
    cv::Mat gray_image;
    cv::cvtColor(image, gray_image, cv::COLOR_BGR2GRAY);

    // Create a copy of the image to draw on.
    cv::Mat marked_image = image.clone();

    // Loop over all pixels in the image.
    for(int c=0; c<image.cols; ++c) {
        for(int r=0; r<image.rows; ++r) {

            // If you think this point is a corner...
            if(gray_image.at<uint8_t>(r, c) < 2) {
                // Mark this point with a blue circle!
                cv::circle(marked_image, cv::Point(c, r), 1.0, cv::Scalar(255,0,0), 1.0);
            }
        }
    }
    return marked_image;
}


int main(int argc, char**argv) {
    // Check that the user provided a path to an image for us to play with.
    if( argc != 2 ) {
        std::cout << "Usage: ./fast my_image.jpg" << std::endl;
    }

    // Read the image in BGR color format.
    cv::Mat img = cv::imread(argv[1], CV_LOAD_IMAGE_COLOR);
    if( !img.data ) {
        std::cout << "Failed to load image." << std::endl;
        return -1;
    }

    // Detect corners in the image. Return a new image with corners marked.
    img = fastDetect(img);

    // Display the results!
    cv::namedWindow("FAST", cv::WINDOW_AUTOSIZE);
    cv::imshow("FAST", img);

    cv::waitKey(0);
    return 0;
}
