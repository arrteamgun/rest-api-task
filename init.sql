CREATE TABLE IF NOT EXISTS questions_quiz (
    id SERIAL PRIMARY KEY,
    question VARCHAR(255) NOT NULL,
    answer VARCHAR(255) NOT NULL,
    creation_date DATE
);