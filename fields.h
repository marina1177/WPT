struct fields_t {
	// Scalar result stored in this variable
	double kpd;

	// 2D I/O array
	double **r1;
};

// Function prototype
void calculate_fields(float a, float b, float c, float e, float lambda, float D, struct fields_t *data);
