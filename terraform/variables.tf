variable "awsregion" {
  default = "us-east-1"
}
variable "instanceTenancy" {
  default = "default"
}
variable "dnsSupport" {
  default = true
}
variable "dnsHostNames" {
  default = true
}


variable "availabilityZoneA" {
  default = "us-east-1a"
}
variable "availabilityZoneB" {
  default = "us-east-1b"
}


variable "vpcCIDRblock" {
  # default = "10.0.0.0/16"
  default = "192.168.0.0/16"
}
variable "privatesCIDRblock1" {
  # default = "10.0.0.0/19"
  default = "192.168.2.0/24"
}
variable "privatesCIDRblock2" {
  # default = "10.0.31.0/19"
  default = "192.168.3.0/24"

}
variable "publicCIDRblock1" {
  # default = "10.0.64.0/19"
  default = "192.168.0.0/24"
}
variable "publicCIDRblock2" {
  # default = "10.0.96.0/19"
  default = "192.168.1.0/24"
}



variable "routeCIDRblock" {
  default = "0.0.0.0/0"
}


