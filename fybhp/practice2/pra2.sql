use activation_code;
CREATE TABLE MyGenerateCode
(
	SerialNumber int(5) NOT NULL,
    ActivationCode char(30) NOT NULL
);
ALTER TABLE MyGenerateCode ADD PRIMARY KEY (SerialNumber);
