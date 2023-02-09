all: neural_net.png chain_rule.png

neural_net.png: neural_net.gv
	dot -Tpng neural_net.gv > neural_net.tmp
	export fileCheck=$$(file neural_net.tmp | cut -d " " -f2)
	export TYP="PNG"
	if [ $$fileCheck = $$TYP ]; then mv neural_net.tmp neural_net.png; fi

chain_rule.png: chain_rule.gv
	dot -Tpng chain_rule.gv > chain_rule.tmp
	export fileCheck=$$(file chain_rule.tmp | cut -d " " -f2)
	export TYP="PNG"
	if [ $$fileCheck = $$TYP ]; then mv chain_rule.tmp chain_rule.png; fi
