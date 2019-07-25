.PHONY: clean rpm

TARGET=prometheus_bot

# commit for GIT_VER is the last original commit before fork
GIT_VER  := $(shell git rev-list e0f5fb28..HEAD --count)
GIT_HASH := $(shell git rev-parse --short HEAD)


all: main.go
	go build -o $(TARGET)
test: all
	prove -v
clean:
	go clean
	rm -f $(TARGET)
	rm -f bot.log
	rm -rf rpm

rpm: $(TARGET)
	rpmbuild -bb \
		--define "_sourcedir ${shell pwd}" \
		--define "_builddir ${shell pwd}" \
		--define "_topdir ${shell pwd}/rpm" \
		--define "_git_ver $(GIT_VER)" \
		--define "_git_hash $(GIT_HASH)" \
		contrib/prometheus_bot.spec
