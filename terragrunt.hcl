# Terragrunt will copy the Terraform configurations specified by the source parameter, along with any files in the
# working directory, into a temporary folder, and execute your Terraform commands in that folder.
terraform {
  source = "../../../../modules//region-wise/s3"
}

# Include all settings from the root terragrunt.hcl file
include {
  path = find_in_parent_folders()
}



locals {
  # Automatically load constant variables
  const_vars = read_terragrunt_config(find_in_parent_folders("consts.hcl"))
  consts     = local.const_vars.locals
  # Automatically load region-level variables
  region_vars = read_terragrunt_config(find_in_parent_folders("region.hcl"))
}

# These are the variables we have to pass in to use the module specified in the terragrunt configuration above
inputs = {
  buckets = [
    {
      name        = "argo-workflow-dev"
      description = "argo workflow dev"
      versioning  = false
    },
  ]
 

}
prevent_destroy = true
