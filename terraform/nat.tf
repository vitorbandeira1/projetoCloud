resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc_proj.id

    tags = {
    Name = "Internet gateway"
  }
}

#---------------NAT_PUBLIC1---------------
resource "aws_eip" "nat_p1" {
  vpc = true

  tags = {
    Name = "Nat 1"
  }
}

resource "aws_nat_gateway" "nat_p1_gw" {
  allocation_id = aws_eip.nat_p1.id
  subnet_id = aws_subnet.public_subnet1.id

  tags = {
    Name = "Nat 1 gateway"
  }

  depends_on = [
    aws_internet_gateway.igw
  ]
}

#---------------NAT_PUBLIC2---------------
resource "aws_eip" "nat_p2" {
  vpc = true

  tags = {
    Name = "Nat 2"
  }
}

resource "aws_nat_gateway" "nat_p2_gw" {
  allocation_id = aws_eip.nat_p2.id
  subnet_id = aws_subnet.public_subnet2.id

  tags = {
    Name = "Nat 2 gateway"
  }

  depends_on = [
    aws_internet_gateway.igw
  ]
}
