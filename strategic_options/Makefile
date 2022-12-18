all: decisionAreas.png

decisionAreas.png: decisionAreas.gv
	dot -Tpng decisionAreas.gv > test.tmp
	export fileCheck=$$(file test.tmp | cut -d " " -f2)
	export TYP="PNG"
	if [ $$fileCheck = $$TYP ]; then mv test.tmp decisionAreas.png; fi
