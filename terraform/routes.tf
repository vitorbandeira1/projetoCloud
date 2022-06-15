#-----------------ROUTE_FOR_PUBLICS-----------------
resource "aws_route_table" "route_table_public_subnet" {  #Apenas 1 route para as duas publics? Sim!
  vpc_id = aws_vpc.vpc_proj.id

  route {
    cidr_block = var.routeCIDRblock
    gateway_id = aws_internet_gateway.igw.id
  }

  tags ={
      Name = "Public Route"
    }
  
}

resource "aws_route_table_association" "route_public_subnet1" {
  subnet_id      = aws_subnet.public_subnet1.id
  route_table_id = aws_route_table.route_table_public_subnet.id
}

resource "aws_route_table_association" "route_public_subnet2" {
  subnet_id      = aws_subnet.public_subnet2.id
  route_table_id = aws_route_table.route_table_public_subnet.id
}




#-----------------ROUTE_FOR_PRIVATES-----------------
resource "aws_route_table" "route_table_private_subnet1" {
  vpc_id = aws_vpc.vpc_proj.id

  route {
    cidr_block = var.routeCIDRblock
    nat_gateway_id = aws_nat_gateway.nat_p1_gw.id
  }

  tags ={
      Name = "Private route 1"
    }
}

resource "aws_route_table" "route_table_private_subnet2" {
  vpc_id = aws_vpc.vpc_proj.id

  route {
    cidr_block = var.routeCIDRblock
    nat_gateway_id = aws_nat_gateway.nat_p2_gw.id
  }

  tags ={
      Name = "Private route 2"
    }
}

resource "aws_route_table_association" "route_private_subnet1" {
  subnet_id      = aws_subnet.private_subnet1.id
  route_table_id = aws_route_table.route_table_private_subnet1.id
}

resource "aws_route_table_association" "route_private_subnet2" {
  subnet_id      = aws_subnet.private_subnet2.id
  route_table_id = aws_route_table.route_table_private_subnet2.id
}

