{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }@attrs:
    flake-utils.lib.eachSystem flake-utils.lib.defaultSystems (system:
    let
      pkgs = import nixpkgs { config.allowUnfree = true; inherit system; };
      in {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            (python3.withPackages (p: with p; [
              ics
            ]))
          ];
        };
      });
}
