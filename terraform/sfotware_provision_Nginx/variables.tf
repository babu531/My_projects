variable "AWS_ACCESS_KEY" {
    default = "AKIA5FJLG5LDGTMAFQA5"
}

variable "AWS_SECRET_KEY" {
    default = "jpbJvLp7O6Jxx1uOstcekHiiHcpjR02ubWEVmyzm"
}

variable "AWS_REGION" {
default = "us-east-2"
}

variable "SECURITY_GROUPS" {
    type = list
    default = ["sg-venky","sg-babu"]
}

variable "AMIS" {
    type = map
    default = {
        us-east-1 = "ami-0f40c8f97004632f9"
        us-east-2 = "ami-05692172625678b4e"
        us-west-2 = "ami-0352d5a37fb4f603f"
        us-west-1 = "ami-0f40c8f97004632f9"
    }
}

variable "script" {
    default = "installNginx.sh"
  
}

variable "PATH_TO_PRIVATE_KEY" {
    default = "mykey"
  
}


variable "PATH_TO_PUBLIC_KEY" {
  default ="mykey.pub"
}

variable "INSTANCE_USERNAME" {
  default = "ubuntu"
}