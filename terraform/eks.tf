#---------------EKS_SETUP---------------
resource "aws_iam_role" "eks_proj" {
  name = "eks_proj"

  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "eks_proj-AmazonEKSClusterPolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.eks_proj.name
}

resource "aws_eks_cluster" "eks_proj" {
  name     = "eks_proj"
  role_arn = aws_iam_role.eks_proj.arn

  vpc_config {
    subnet_ids = [
      aws_subnet.private_subnet1.id,
      aws_subnet.private_subnet2.id,
      aws_subnet.public_subnet1.id,
      aws_subnet.public_subnet2.id
    ]
  }

  depends_on = [aws_iam_role_policy_attachment.eks_proj-AmazonEKSClusterPolicy]
}