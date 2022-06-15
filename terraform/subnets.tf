#---------------SUBNETS---------------
resource "aws_subnet" "private_subnet1" {
  vpc_id     = aws_vpc.vpc_proj.id
  cidr_block = var.privatesCIDRblock1

  map_public_ip_on_launch = "false"
  availability_zone = var.availabilityZoneA # Posso colocar todas as subnets na mesma zone? Nao

  tags = {
    "Name"                        = "Private1"
    "kubernetes.io/role/elb"      = "1"
    "kubernetes.io/cluster/eks"   = "shered"
  }

}
resource "aws_subnet" "private_subnet2" {
  vpc_id     = aws_vpc.vpc_proj.id
  cidr_block = var.privatesCIDRblock2
  
  map_public_ip_on_launch = "false"
  availability_zone = var.availabilityZoneB

  tags = {
    "Name"                        = "Private2"
    "kubernetes.io/role/elb"      = "1"
    "kubernetes.io/cluster/eks"   = "shered"
  }

}
resource "aws_subnet" "public_subnet1" {
  vpc_id     = aws_vpc.vpc_proj.id
  cidr_block = var.publicCIDRblock1

  map_public_ip_on_launch = "true"
  availability_zone = var.availabilityZoneA
  
  tags = {
    "Name"                        = "Public1"
    "kubernetes.io/role/elb"      = "1"
    "kubernetes.io/cluster/eks"   = "shered"
  }

}
resource "aws_subnet" "public_subnet2" {
  vpc_id     = aws_vpc.vpc_proj.id
  cidr_block = var.publicCIDRblock2
  
  map_public_ip_on_launch = "true"
  availability_zone = var.availabilityZoneB
  
  tags = {
    "Name"                        = "Public2"
    "kubernetes.io/role/elb"      = "1"
    "kubernetes.io/cluster/eks"   = "shered"
  }

}

